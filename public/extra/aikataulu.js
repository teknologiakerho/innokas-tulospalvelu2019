const renderXsumo = event => live.timetable.renderEvent({
	clazz: "live-timetable-xsumo",
	badge: { icon: "/xsumo-logo.svg", text: "XSumo" },
	teams: event.teams,
	arena: event.arena
});

const renderRescue = event => live.timetable.renderEvent({
	clazz: "live-timetable-res",
	badge: {
		icon: "/rescue-logo.svg",
		text: event.block.id.includes("haast") ? "Rescue (haastattelu)" : "Rescue"
	},
	teams: event.teams,
	arena: event.arena
});

const renderDance = event => live.timetable.renderEvent({
	clazz: "live-timetable-dance",
	badge: {
		icon: "/tanssi-logo.svg",
		text:
			event.block.id.includes("haast") ? "Tanssi (haastattelu)" :
			event.block.id.includes("harj") ? "Tanssi (harjoitus)" :
			"Tanssi/Teatteri"
	},
	teams: event.teams,
	arena: event.arena
});

live.config({
	api: "http://kisat2019.teknologiakerho.fi/api"
});

live.carousel([

	live.page("#page-timetable", {
		timeout: 120 * 1000,
		components: [
			live("timetable", "#timetable", {
				interval: 10000,
				rules: [
					event => event.block.id.startsWith("xs") && renderXsumo,
					event => event.block.id.startsWith("rescue") && renderRescue,
					event => event.block.id.startsWith("tanssi") && renderDance
				]
			})
		]
	})

]);
