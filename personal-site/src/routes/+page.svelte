<script>
	import ContentCard from "$lib/ContentCard.svelte"
	import Publication from "$lib/Publication.svelte"
	import orcidLogo from "$lib/assets/orcid_16x16.webp"
	import ayresImage from "$lib/assets/aryes.webp"


	let publications = [
		{
			articleTitle: "Structural stability of REE-PO<sub>4</sub> (REE= Sm, Tb) under swift heavy ion irradiation",
			articleLink: "https://www.sciencedirect.com/science/article/pii/S0168583X22001884?casa_token=NDOnXPWF0BAAAAAA:1EnhthpOBogAEzW95kY0SdFCxQIDJxv54Wfj-lGLCR3f6jtLqRFmqg_WbEaE-gh44GlL6sMRtlY",
			journalName: "Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms",
			abstract: "Rare earth element (REE) phosphates are an attractive host matrix for long-lived radionuclides from nuclear waste because of the radiation tolerance exhibited by naturally occurring REE phosphate specimens. Here we show that SmPO<sub>4</sub> (monazite structure) and TbPO<sub>4</sub> (xenotime structure) exhibit a similar amorphization response to swift heavy ion irradiation despite different starting structures. SmPO4 and TbPO4 were irradiated with 1.1 GeV Au ions and analyzed using synchrotron-based X-ray diffraction (XRD), Raman spectroscopy, and transmission electron microscopy (TEM). The radiation response of the phosphates was evaluated by extracting the amorphous fraction at each irradiation fluence, and a single-impact model was used to determine the amorphous cross section and track diameter. Amorphization within individual ion tracks was confirmed using head-on TEM imaging, and the amorphous track size agreed with the value deduced by XRD analysis. Raman measurements were performed to qualitatively confirm the ion-induced crystalline-to-amorphous transformation which proceeds similarly for both phosphates."
		},
		{
			articleTitle: "Comparison of short-range order in irradiated dysprosium titanates",
			articleLink: "https://www.nature.com/articles/s41529-021-00165-6",
			journalName: "npj Materials Degradation",
			abstract: "The structural response of Dy<sub>2</sub>TiO<sub>5</sub> oxide under swift heavy ion irradiation (2.2 GeV Au ions) was studied over a range of structural length scales utilizing neutron total scattering experiments. Refinement of diffraction data confirms that the long-range orthorhombic structure is susceptible to ion beam-induced amorphization with limited crystalline fraction remaining after irradiation to 8 × 10<sup>12</sup> ions/cm<sup>2</sup>. In contrast, the local atomic arrangement, examined through pair distribution function analysis, shows only subtle changes after irradiation and is still described best by the original orthorhombic structural model. A comparison to Dy<sub>2</sub>Ti<sub>2</sub>O<sub>7</sub> pyrochlore oxide under the same irradiation conditions reveals a different behavior: while the dysprosium titanate pyrochlore is more radiation resistant over the long-range with smaller degree of amorphization as compared to Dy<sub>2</sub>TiO<sub>5</sub>, the former involves more local atomic rearrangements, best described by a pyrochlore-to-weberite-type transformation. These results highlight the importance of short-range and medium-range order analysis for a comprehensive description of radiation behavior."	
		}
	];

</script>

<main>
	<ContentCard>
		<span slot="title">Education</span>
		<div slot="content">
			<p>BS in Nuclear Engineering at the University of Tennessee Knoxville</p>
			<div id="education-content">
				<div style="width: 40%">
					<p>GPA – 3.86/4.0</p>
					<br>
					<ul>
						<li>Outstanding Undergraduate Research Award for the nuclear engineering department.</li>
    					<li>Top Freshmen Academic Performer Award for the nuclear engineering department.</li>
					</ul>

					<br>

					<p>Related Coursework:</p>
					<ul>
						<li>Introduction to Nuclear and Radiological Engineering</li>
						<li>Differential Equations                              </li>
						<li>Honors Engineering Fundamentals                     </li>
						<li>Electricity and Magnetism                           </li>
						<li>Introduction to Nuclear Physics                     </li>
						<li>Nuclear System Dynamics and Control                 </li>
						<li>Thermal Science                                     </li>
						<li>Radiological Engineering Laboratory                 </li>
						<li>Nuclear Reactor Theory                              </li>
					</ul>

				</div>
				<img src={ayresImage} style="width: min(300px, 100%); height: auto; object-fit: cover"/>
			</div>
		</div>
	</ContentCard>

	<ContentCard>
		<span slot="title">Research</span>
		<div slot="content">
			<p>My research is on characterizing material responses to extreme conditions: specificially, intense radiation environments and energetic processing methods such as ball milling. The group I am in uses a combination of techniques - neutron total scattering (<a href="https://neutrons.ornl.gov/sns">Spallation Neutron Source</a> at ORNL), synchrotron X-ray diffraction (<a href="https://www.aps.anl.gov/">Advanced Photon Source</a> at ANL and the <a href="https://www.bnl.gov/nsls2/">National Synchrotron Light Source II at BNL</a>).</p>

			<br>
			<h2>Published Work</h2>
			<br>
			<p><img src={orcidLogo}> <a href="https://orcid.org/0000-0001-6595-3767">0000-0001-6595-3767</a><p>
			<br>

			<div id="publication-list">
				{#each publications as d}
					<Publication {...d}></Publication>
				{/each}
			</div>
		</div>
	</ContentCard>

	<ContentCard>
		<span slot="title">Interests</span>
		<div id="interests" slot="content">
			<ContentCard>
				<span slot="title">Coding</span>
				<div slot="content">
					<p></p>
				</div>
			</ContentCard>

			<ContentCard>
				<span slot="title">Coding</span>
			</ContentCard>

			<ContentCard>
				<span slot="title">Guitar</span>
			</ContentCard>

			<ContentCard>
				<span slot="title">Guitar</span>
			</ContentCard>
		</div>
	</ContentCard>
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-color: var(--clr-background);
	}

	#interests {
		columns: 3 350px;	
	}

	main > h1 {
		text-align: center;
		opacity: 0.7;
		margin: 1em 0;
	}

	ol {
		list-style: none;
		margin-left: 1rem;
	}

	ul {
		list-style: disc;
		margin-left: 1.5rem;
	}

	#publication-list {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	#education-content {
		display: flex;
		flex-wrap: wrap;
		flex-direction: row;
		column-gap: 1rem;
		row-gap: 1rem;
		justify-content: center;
		padding: 1rem;
	}

	#education-content > * {
		flex-grow: 1;
	}
</style>
