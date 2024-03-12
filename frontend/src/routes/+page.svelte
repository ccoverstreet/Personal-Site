<script>
	import Toolbar from "$lib/Toolbar.svelte";
	import GalleryCard from "$lib/GalleryCard.svelte";

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
				out += "<a href='https://scholar.google.com/citations?hl=en&user=YYSBgjoAAAAJ' style='color: #000 '><em style='font-weight: bold;'>Cale Overstreet</em></a>"
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
</script>


<Toolbar/>


<div style="mask-image: linear-gradient(to bottom, black calc(100% - 48px), transparent 100%);
height: calc(100vh - 3rem); overflow-y: scroll;
">

	<div id="banner" style="">
		<div style="
		display: flex;
		height: 100%;
		width: 100%;
		color: #E6E6E6;
		font-weight: bold;
		font-size: 3rem;
		align-items: center;
		justify-content: center;
		">
			<div style="
			display: flex;
			justify-content: center;
			align-items: center;
			flex-direction: column;
			margin: 2rem 2rem;
			padding: 2rem;
			background-color: rgba(0, 0, 0, 0.7);
			border: 1px solid #eeeeee;
			">
				<div>
					Cale Overstreet
				</div>

				<div style="font-size: 1rem; color: #bbbbbb; margin-top: 2rem;">
					PhD Student at the University of Tennessee Knoxville
				</div>
			</div>
		</div>

	</div>

	<div class="section">

		<div id="about-me" class="section-content" style="color:#bbbbbb;  background-color: #0C0C13;">
			<div style="height: 30rem; display: flex; justify-content: center; align-items: center">
				<img src="/headshot.jpg" style="
				width: auto; height: 100%; object-fit: contain; margin: 1rem 0.5rem;;"/>
			</div>

			<div>
				<h1>About Me</h1>
				<p style="color: #bbbbbb; padding: 0.5rem; font-size: 1.25rem;">
					Welcome to my site! I am Cale Overstreet, a Ph.D. student at the University of Tennessee Knoxville in the Nuclear Engineering Department, specializing in the study of amorphous phases of complex oxides and their ceffects on physical properties. I have had the privilege of performing experiments at national and international user facilities, including the Spallation Neutron Source at Oak Ridge National Laboratory, Advanced Photon Source at Argonne National Laboratory, National Synchrotron Light Source II at Brookhaven National Laboratory, GSI Helmholtz Centre for Heavy Ion Research, and the DC-60 cyclotron at the Joint Institute for Nuclear Research in Kazakhstan. I hold an undergraduate degree in nuclear engineering from the University of Tennessee Knoxville, which provided me me with a solid foundation for my current academic pursuits.

					<br>
					<br>

					Beyond the academic sphere, I enjoy learning and becoming proficient with programming, which serves both as a research tool and a personal pursuit. In my free-time, I enjoy playing guitar and exploring Knoxville through cycling.

				</p>
			</div>
		</div>
	</div>

	<div class="section" style=""> 
		<div class="section-header" style="color: #eeeeee; background-color: #476473">
			<h1>Research</h1>
		</div>

		<div class="section-content" style="background-image: url('/daiscund.png'); background-size: fill; background-position: center;">
			<div class="section-card" style="color:#333333">
				<div class="section-header">
					<h2>Publications</h2>
				</div>

				<div>
					<ul>
						{#each publications as pub}
							<li >
								<a href="{pub.link}" style="color: #333333;"><em>{pub.title} ({pub.date})</em></a>
								<br>

								<p>
									{@html authorsToHTML(pub.authors)}
								</p>

								<em>{pub.journal}</em>
							</li>
						{/each}
					</ul>
				</div>

				<br>

			</div>

			<div class="section-card">
				<h2>Gallery</h2>
				<div id="gallery-holder" style="display: flex; flex-wrap: wrap; justify-content: center">
					{#each pictures as p}
						<GalleryCard imageName={p.imageName} description={p.description}/>
					{/each}
				</div>
			</div>
		</div>
	</div>

	<div style="background-color: #2A2E32; height: 3rem; width: 100vw;">
	</div>
</div>


<style>

	#banner {
		height: 50vh;
		width: 100vw;
 	 	background-image: url(/daiscund.jpg);
 		background-size: cover;
 		background-position: center;
	}

	em {
		font-style: italic;
	}

	li {
		margin-bottom: 1rem;
		line-height: 1.5rem;
	}

	h1 {
		font-size: 2rem;
		font-weight: bold;
		margin: 1rem 1rem;
	}


	h2 {
		font-size: 1.5rem;
		font-weight: bold;
		margin: 1rem 0rem;
		color: #333333;
	}

	.section {
		display: flex;
		justify-content:center;
		flex-direction: row;
		flex-wrap: wrap;
	}

	.section-header {
		width: calc(100% - 2rem);
		padding: 1rem;
		display: flex;
		justify-content: center;
	}

	.section-content {
		display: flex;
		flex-direction: row;
		justify-content: center;
		width: 100%;
	}

	.section-card {
		background-color: #eeeeee;
		padding: 1rem;
		max-width: 100ch;
		min-width: 40ch;
		margin: 1rem;
		width: calc(100% - 4rem);
		box-shadow: 0.25rem 0.25rem 1rem black;
	}

	p {
		line-height: 1.5rem;
	}

	p > br {
		margin-top: 0rem;
	}


	#about-me {
		display: flex;
	}
	#about-me > * {
		max-width: 80ch;
		min-width: 40ch;
		align-items: center;
	}

	#gallery-holder > * {
		flex-grow: 1;
	}
</style>
