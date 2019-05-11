const renderXsumo = event => live.timetable.renderEvent({
	clazz: "live-timetable-xsumo",
	teams: event.teams,
	arena: event.arena
});

live.config({
	api: "http://kisat2019.teknologiakerho.fi/api"
});

live.carousel([

	live.page("#timetable", {
		timeout: 120 * 1000,
		components: [
			live("timetable", "#timetable", {
				arenas: ["XSumo1"],
				limit: 8,
				rules: [
					event => event.arena.startsWith("XSumo") && renderXsumo,
					/* Muita tässä ei pitäskään olla */
				]
			})
		]
	})

]);

// XXX tunge tää liveen
const $clock = document.getElementById("clock");
const updateClock = () => {
	const date = new Date();
	const p2 = n => (n+"").padStart(2, "0");
	$clock.innerHTML = `${p2(date.getHours())}:${p2(date.getMinutes())}:${p2(date.getSeconds())}`;
};

updateClock();
setInterval(updateClock, 100);
