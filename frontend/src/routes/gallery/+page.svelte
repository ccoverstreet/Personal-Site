<script>
	import Toolbar from "$lib/Toolbar.svelte";
	import GalleryCard from "$lib/GalleryCard.svelte";
	import LinkCard from "$lib/LinkCard.svelte";

	const publications = [
		{
			title: "Structural stability of REE-PO4 (REE=Sm,Tb) under swift heavy ion irradiation",
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
			title: "Systematic study of short-and long-range correlations in RE 3 TaO 7 weberite-type compounds by neutron total scattering and X-ray diffraction",
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

	function authorsToHTML(authors) {
		console.log(authors);
		var out = "";
		for (const [i,a] of authors.entries()) {
			if (i > 0) {
				out += ", "
			}

			if (a === "Cale Overstreet") {
				out += "<a href='https://scholar.google.com/citations?hl=en&user=YYSBgjoAAAAJ' style='color: var(--clr-font-white-high) '><em style='font-weight: bold;'>Cale Overstreet</em></a>"
			} else {
				out += a;
			}
		}

		return out
	}

	const pictures = [
		{
			imageName: "REI-presentation.jpg",
			description: "Oral presentation at the Radiation Effects in Insulators (REI) 21 conference in Fukuoka, Japan (September 2023) on 'Characterizing swift heavy ion-induced amorphous phases in complex oxides'"
		},
		{
			imageName: "REI-group-photo.jpg",
			description: "Photo of participants at Radiation Effects in Insulators (REI) 21 conference in Fukuoka, Japan (September 2023)"
		},
	]

	const linkCards = [
		{
			title: "Research",
			subtitle: "Characterization and analysis of amorphous phases of complex oxides",
			imageSrc: "REI-presentation.jpg",
			link: "/research"
		},
		{
			title: "Gallery",
			subtitle: "Random photos from research/travel/personal",
			imageSrc: "daiscund.jpg",
			link: "/gallery"
		},
		{
			title: "Projects",
			subtitle: "Personal projects",
			imageSrc: "CCOEspLight.JPG",
			link: "/projects"
		}
	]
</script>


<Toolbar/>

<div id="daiscund">

	<div id="intro-banner">

		<h1>
			Cale Overstreet
		</h1>

		<h2 style="max-width: 40rem;">
			Nuclear Engineering PhD Student at the University of Tennessee Knoxville
		</h2>

	</div>

	<div id="main-content">
		<div id="about-me" class="card">
			<div class="card-header">
				<h1>About Me</h1>
			</div>

			<div style="display: flex; flex-wrap: wrap; padding: 1rem;">
				<p style="min-width: 10ch;">
					Welcome to my site! I am Cale Overstreet, a Ph.D. student at the University of Tennessee Knoxville in the Nuclear Engineering Department, specializing in the study of amorphous phases of complex oxides and their ceffects on physical properties. I have had the privilege of performing experiments at national and international user facilities,  I hold an undergraduate degree in nuclear engineering from the University of Tennessee Knoxville, which provided me me with a solid foundation for my current academic pursuits.

					<br>
					<br>

					Beyond the academic sphere, I enjoy learning and becoming proficient with programming, which serves both as a research tool and a personal pursuit. In my free-time, I enjoy playing guitar and exploring Knoxville through cycling.
				</p>

			</div>

		</div>

		{#each linkCards as lc}
			<LinkCard title={lc.title} subtitle={lc.subtitle} imageSrc={lc.imageSrc} link={lc.link}/>
		{/each}
		
	</div>


	<div style="height: 100vh">
	</div>

</div>

<style>
	#daiscund {
		background: linear-gradient(rgba(0, 0, 0,0.8), rgba(255, 255, 255, 0.2)), url("/daiscund.jpg");
		background-size: cover;
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	#intro-banner > * {
		min-width: 10rem;
		flex-grow: 1;
		height: 7rem;
		text-align: center;
		align-items: center;
		font-size: 4rem;
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		font-weight: bold;
		justify-content: center;
	}

	#intro-banner > h1 {
		color: var(--clr-font-white-high);
	}

	#intro-banner > h2 {
		font-size: 2rem;
		color: var(--clr-font-white-low);
	}


	#main-content {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	#main-content > * {
		flex: 1;
		min-width: 20rem;
	}

	#about-me {
		background-color: var(--clr-gray);
		font-size: 1.1rem;
	}

	#publications > ul > li {
		margin-bottom: 1rem;
	}

	#gallery {
		overflow-y: scroll;
	}

	#gallery-content {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	#gallery-content > * {
		flex-grow: 1;
	}

</style>


