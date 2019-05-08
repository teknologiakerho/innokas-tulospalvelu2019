import flask
import robostat
import robostat.db
import robostat.web.db
from robostat.tournament import aggregate_scores, sort_ranking, decode_block_scores,\
        tiebreak_ranking, combine_ranks
from robostat.rulesets.xsumo import XSRuleset, XSumoScoreRank
from robostat.rulesets.rescue import RescueRuleset, RescueMaxRank
from robostat.rulesets.haastattelu import HaastatteluRuleset
from robostat.web.util import get_block
from robostat.web.views.ranking import details_renderer, make_block_renderer, card_renderer
from robostat.web.views.ranking.renderers import render_xsumo_matrix, rescue_card_renderer
from robostat.web.views.timetable import event_renderer

class OtherRuleset(HaastatteluRuleset):
    def __init__(self, name):
        self.name = name

@event_renderer.of(OtherRuleset)
def render_other_event(event):
    return flask.render_template("timetable/event-other.html",
            event=event,
            name=get_block(event).ruleset.name
    )

xsumo_ruleset = XSRuleset()
rescue1_ruleset = RescueRuleset.by_difficulty(1, max_time=600)
rescue2_ruleset = RescueRuleset.by_difficulty(2, max_time=600)
rescue3_ruleset = RescueRuleset.by_difficulty(3, max_time=600)
esitys_ruleset = OtherRuleset("Esitys")
esittely_ruleset = OtherRuleset("Esittely")
harjoittelu_ruleset = OtherRuleset("Harjoittelu")
haastattelu_ruleset = HaastatteluRuleset()

# xsumo ranking tiebreakerilla
def xsumo_tb(id, name):

    block = robostat.block(id=id, name=name, ruleset=xsumo_ruleset)

    @robostat.ranking(block.id, name=block.name)
    @details_renderer(make_block_renderer(block, render_xsumo_matrix))
    def ranking_tb(db):
        scores = block.decode_scores(db, hide_shadows=True)
        ranks = aggregate_scores(scores, XSumoScoreRank.from_scores)
        tiebreaks = tiebreak_ranking(db, block.id)
        combined = combine_ranks(ranks, tiebreaks)
        return sort_ranking(combined.items())

# xsumo ranking ilman tiebreakeria
def xsumo_notb(id, name):

    block = robostat.block(id=id, name=name, ruleset=xsumo_ruleset)

    @robostat.ranking(block.id, name=block.name)
    @details_renderer(make_block_renderer(block, render_xsumo_matrix))
    def ranking(db):
        scores = block.decode_scores(db, hide_shadows=True)
        ranks = aggregate_scores(scores, XSumoScoreRank.from_scores)
        return sort_ranking(ranks.items())

# rescue ranking, kaksi suoritusta joista paras valitaan
def rescue(ruleset, id, name):
    
    block1 = robostat.block(
            id="%s.1" % id,
            name="%s kierros 1" % name,
            ruleset=ruleset
    )

    block2 = robostat.block(
            id="%s.2" % id,
            name="%s kierros 2" % name,
            ruleset=ruleset
    )

    # Haastattelut, näille ei ole rankingia
    robostat.block(
            id="%s.haast" % id,
            name="%s haastattelut" % name,
            ruleset=haastattelu_ruleset
    )

    @robostat.ranking(id, name=name)
    @card_renderer(rescue_card_renderer(ruleset))
    def rescue_ranking(db):
        scores = decode_block_scores(db, block1, block2, hide_shadows=True)
        ranks = aggregate_scores(scores, RescueMaxRank.from_scores)
        return sort_ranking(ranks.items())

# tanssit vain aikataulujen takia
def tanssi(id, name):

    robostat.block(
            id="%s.haast" % id,
            name="%s haastattelut" % name,
            ruleset=haastattelu_ruleset
    )

    robostat.block(
            id="%s.harj" % id,
            name="%s harjoittelut" % name,
            ruleset=harjoittelu_ruleset
    )

    robostat.block(
            id="%s.esitys" % id,
            name="%s esitykset" % name,
            ruleset=esitys_ruleset
    )

# 8 alkusarja1 lohkoa, näistä
# * 2 parasta pääsee suoraan jatkoon
# * 5 seuraavaa pääsee alkusarja 2
# * Loput joutuvat säälisarjaan josta ei voi päästä jatkoon
for i in range(1, 9):
    xsumo_tb("xs.as1.%d" % i, "XSumo alkusarja 1, lohko %d" % i)

# 4 alkusarja1 lohkoa, voittajat pääsevät jatkoon
for i in range(1, 5):
    xsumo_tb("xs.as2.%d" % i, "XSumo alkusarja 2, lohko %d" % i)

# 3 säälisarja lohkoa, näistä ei pääse jatkoon
for i in range(1, 4):
    xsumo_notb("xs.ss.%d" % i, "XSumo alkusarja 3, lohko %d" % i)

# 2 jatkosarjan lohkoa, näistä
# * Lohkon 1 voittaja ja lohkon 2 toinen pelaavat toisiaan vastaan
# * Lohkon 2 voittaja ja lohkon 1 toinen pelaavat toisiaan vastaan
# * Voittajat jatkavat finaaliin, häviäjät pronssiotteluun
xsumo_tb("xs.js.1", "XSumo jatkosarja, lohko 1")
xsumo_tb("xs.js.2", "XSumo jatkosarja, lohko 2")

# Semifinaalit
xsumo_notb("xs.semi.1", "XSumo semifinaali 1")
xsumo_notb("xs.semi.2", "XSumo semifinaali 2")

# Finaalit
xsumo_notb("xs.final", "XSumo finaali")
xsumo_notb("xs.pronssi", "XSumo pronssiottelu")

# Yleinen karsintalohko, jos tarvitsee pelata
robostat.block(id="xs.karsinta", name="XSumo karsinta", ruleset=xsumo_ruleset)

# Rescuet, kaikissa
# * 2 suoritusta per joukkue, kummatkin eri päivinä
# * Paras jää voimaan
# * Haastattelut (ei arvioida)
rescue(rescue1_ruleset, "rescue1", "Rescue 1")
rescue(rescue2_ruleset, "rescue2", "Rescue 2")
rescue(rescue3_ruleset, "rescue3", "Rescue 3")

# Tanssit vain aikataulun takia
tanssi("tanssi.alkeis", "Tanssi Alkeissarja")
tanssi("tanssi.jatko", "Tanssi Jatkosarja")
