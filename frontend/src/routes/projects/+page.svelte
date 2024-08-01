<script>
	import Toolbar from "$lib/Toolbar.svelte";
	import LinkCard from "$lib/LinkCard.svelte";

	let projects = [
		{
			name: "DISMAT Utils",
			description: "Script and application repository for the DISMAT group at UTK",
			link: "https://github.com/ccoverstreet/DISMAT-Utils",
			imageSrc: "/DISMAT-Utils-preview.png",
		},
		{
			name: "Forestry",
			description: "Desktop-environment agnostic settings application for Linux systems",
			link: "https://github.com/ccoverstreet/Forestry",
			imageSrc: "/network-page.png",
		},
		{
			name: "Salad Notes",
			description: "Locally hosted markdown notetaking system with web editor",
			link: "https://github.com/ccoverstreet/salad-notes",
			imageSrc: "/salad-notes.png",
		},
	]
</script>

<Toolbar/>

<div id="content">
	<div id="intro-banner">
		<h1>Projects</h1>
	</div>

	<div id="project-cards">
		{#each projects as project}
			<LinkCard title={project.name} subtitle={project.description} imageSrc={project.imageSrc} link={project.link}/>
		{/each}
	</div>
</div>

<style>
	#intro-banner > * {
		min-width: 10rem;
		flex-grow: 1;
		height: 8rem;
		text-align: center;
		align-items: center;
		font-size: 4rem;
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		font-weight: bold;
		justify-content: center;
		flex-direction: column;
	}

	#intro-banner > h1 {
		width: 100%;
		color: var(--clr-font-white-high);
	}

	#intro-banner > h2 {
		width: 100%;
		font-size: 2rem;
		color: var(--clr-font-white-low);
	}


	#content {
		background: linear-gradient(rgba(0, 0, 0,0.8), rgba(255, 255, 255, 0.2)), url("/daiscund.jpg");
		background-size: cover;
		display: flex;
		flex-direction: column;
		flex-wrap: wrap;
		justify-content: center;
		min-height: 100vh;
	}

	#project-cards {
		display: flex;
		flex-wrap: wrap;
		flex-direction: row;
		justify-content: center;
	}

	#project-cards > * {
		min-width: 40ch;
		max-width: 45ch;
	}
</style>
