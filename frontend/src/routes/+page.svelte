<script>
	import Toolbar from "$lib/Toolbar.svelte";
	import LinkCard from "$lib/LinkCard.svelte";

	const publications = [
		{
			title: "Structural stability of REE-PO<sub>4</sub> (REE=Sm,Tb) under swift heavy ion irradiation",
			authors: ["Cale Overstreet", "Jacob Cooper", "Eric O'Quinn", "William Cureton", "Raul Palomares", "Julia Leys", "Guido Deissmann", "Stefan Neumeier", "Chien-Hung Chen", "Maik Lang"],
			journal: "Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms",
			date: "2022",
			link: "https://www.sciencedirect.com/science/article/pii/S0168583X22001884",
		},
		{
			title: "Comparison of short-range order in irradiated dysprosium titanates",
			authors: ["Roman Sherrod", "Eric C O’Quinn", "Igor M Gussev", "Cale Overstreet", "Joerg Neuefeind", "Maik K Lang"],
			journal: "npj Materials Degradation",
			date: "2021",
			link: "https://www.nature.com/articles/s41529-021-00165-6"
		},
		{
			title: "Systematic study of short-and long-range correlations in RE<sub>3</sub>TaO<sub>7</sub> weberite-type compounds by neutron total scattering and X-ray diffraction",
			authors: ["Igor M Gussev", "Eric C O'Quinn", "Matthew Tucker", "Rodney C Ewing", "Cale Overstreet", "Jörg Neuefeind", "Michelle Everett", "Qiang Zhang", "David Sprouster", "Daniel Olds", "Gianguido Baldinozzi", "Maik Lang"],
			journal: "Journal of Materials Chemistry A",
			date: "2023",
			link: "https://www.nature.com/articles/s41529-021-00165-6"
		},
		{
			title: "Swift heavy ion irradiation effects in zirconium and hafnium carbides",
			authors: ["Evan Williams", "Jacob Minnette", "Eric O'Quinn", "Alexandre Solomon", "Cale Overstreet", "William F Cureton", "Ina Schubert", "Christina Trautman", "Changyong Park", "Maxim Zdorovets", "Maik Lang"],
			journal: "Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms",
			date: "2024",
			link: "https://www.sciencedirect.com/science/article/pii/S0168583X2400017X"
		}
	].sort((a, b) => {
		return a.date < b.date ? true : false;
	});

	const presentations = [
		{
			title: "Characterizing swift heavy ion-induced amorphous phases in complex oxides",
			date: "2023-09-05",
			conference: "Conference on Radiation Effects in Insulators 21",
			location: "Fukuoka, Japan"
		},
		{
			title: "Structural Stability of REE-PO<sub>4</sub> (REE=Sm,Tb) under Swift Heavy Ion Irradiation",
			date: "2023-10-02",
			conference: "Materials Science & Technology 23",
			location: "Columbus, Ohio"
		},
		{
			title: "Magnetic Properties of Non-Crystalline Ho<sub>2</sub>Ti<sub>2</sub>O<sub>7</sub> Pyrochlore Prepared by Far-From-Equilibrium Processing",
			date: "2024-10-05",
			conference: "Materials Science & Technology 24",
			location: "Pittsburgh, Pennsylvania"
		}
	].sort((a, b) => {
		return a.date < b.date ? true : false;
	});

</script>


<div id="intro-header" class="banner">
	<Toolbar/>
	<h1>Cale Overstreet</h1>
	<p id="intro-text">
		I am a Ph.D. student at the University of Tennessee Knoxville in the Nuclear Engineering Department, with an undergraduate degree in nuclear engineering from the University of Tennessee Knoxville, specializing in the study of amorphous phases of complex oxides and their associated physical properties. 
	</p>
</div>



<div class="section-centered"> 
	<div class="section-header">
		<h2>Publications</h2>
	</div>

	<div>
	{#each publications as pub}
		<div class="pub-section">
			<a href="{pub.link}"><p class="pub-title">{pub.title} (<span style="font-weight: bold;">{pub.date}</span>)</p></a>
			<p class="pub-journal">{pub.journal}</p>
			<p class="pub-authors">
				{#each pub.authors as auth, i}
					{#if auth.includes("Cale")}
						<span style="font-weight: bold;">{auth},&nbsp</span>
					{:else if i === pub.authors.length - 1}
						{auth}
					{:else}
						{auth},&nbsp  
					{/if}
				{/each}
			</p>
		</div>
	{/each}
	</div>
</div>

<div class="section-full">
	<div class="section-full-content">
		<h2 >Presentations</h2>
		
		<br>
		<div>
			{#each presentations as pres}
				<div style="padding: 0.5rem;">
					<p style="font-style: italic">{@html pres.title}</p> 
					<p>{pres.date}</p>
					<p>{pres.conference}</p>
					<p>{pres.location}</p>
				</div>
			{/each}
		</div>

	</div>

	<img src="/REI-presentation.jpg"/>
</div>


<style>
	.banner {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100%;
		background: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url("/daiscund.jpg");
		background-size: cover;
	}


	#intro-header > h1 {
		font-size: 4rem;
		font-weight: bold;
		color: #dddddd;
		padding: 2rem 0.5rem;
	}

	#intro-text {
		padding: 1rem;
		font-size: 1.25rem;
		line-height: 2rem;
		text-align: center;
		color: #cccccc;
		max-width: 40rem;
	}

	.section-header {
		display: flex;
		width: 100%;
		justify-content: center;
		margin-top: 2rem;
		margin-bottom: 3rem;
	}

	.section-centered {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		padding: 1rem;
	}

	.section-centered > * {
		max-width: 80rem;
	}

	.section-full {
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: #f6f6f6;
		flex-wrap: wrap;
	}

	.section-full > * {
		flex-grow: 1;
		min-width: 0rem;
		width: 100%;
		max-width: 40rem;
	}

	.section-full > img  {
	}

	.section-full-content {
		padding: 2rem;
	}

	h2 {
		font-size: 2.5rem;
		font-weight: bold;
		color: var(--color-2);
	}

	.pub-section {
		padding: 1rem;
	}

	.pub-section > * {
		margin: 0.5rem 0;
	}

</style>
