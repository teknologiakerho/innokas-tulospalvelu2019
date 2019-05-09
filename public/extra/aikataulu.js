const renderXsumo = event => live.timetable.renderEvent({
	clazz: "live-timetable-xsumo",
	badge: { icon: "/xsumo-logo.svg", text: "XSumo" },
	teams: event.teams,
	arena: event.arena
});

const renderRescue = event => live.timetable.renderEvent({
	clazz: "live-timetable-res",
	badge: { icon: "/rescue-logo.svg", text: "Rescue" },
	teams: event.teams,
	arena: event.arena
});

const renderDance = event => live.timetable.renderEvent({
	clazz: "live-timetable-dance",
	badge: { icon: "/tanssi-logo.svg", text: "Tanssi/Teatteri" },
	teams: event.teams,
	arena: event.arena
});

live.config({
	api: "http://kisat2019.teknologiakerho.fi/api"
});

live.carousel([

	live.page("#page-timetable", {
		timeout: 60 * 1000,
		components: [
			live("timetable", "#timetable", {
				interval: 10000,
				/*
				blocks: [
					"rescue1.1", "rescue1.2",
					"tanssi.alkeis.esitys", "tanssi.jatko.esitys"
				],
				*/
				rules: [
					event => event.block.id.startsWith("xs") && renderXsumo,
					event => event.block.id.startsWith("rescue") && renderRescue,
					event => event.block.id.startsWith("tanssi") && renderDance
				]
			})
		]
	})

]);
