live.config({
	api: "http://kisat2019.teknologiakerho.fi/api"
});

const timeout = 30 * 1000;

const carousel = live.carousel(

	[[1, 2], [3, 4], [5, 6], [7, 8]].map(blocks => live.page(`#page-${blocks.join("")}`, {
		timeout,
		components: blocks.map(b =>
			live("ranking", `#ranking-as1-${b}`, {
				id: `xs.as1.${b}`,
				renderer: "xsumo",
				limit: 5
			})
		)
	}))

);

live.keycontrol(carousel);
