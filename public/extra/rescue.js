live.config({
	api: "http://kisat2019.teknologiakerho.fi/api"
});

const timeout = 30 * 1000;

const carousel = live.carousel(

	[1, 2, 3].map(r => live.page(`#page-rescue-${r}`, {
		timeout,
		components: [
			live("ranking", `#ranking-rescue-${r}`, {
				id: `rescue${r}`,
				renderer: "rescue"
			})
		]
	}))

);

live.keycontrol(carousel);
