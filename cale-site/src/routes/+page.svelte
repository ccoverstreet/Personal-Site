<script>
	import Toolbar from "$lib/Toolbar.svelte";
</script>


<Toolbar/>
<div id="banner" style="
">
	<div style="
	display: flex;
	height: 100%;
	width: 100%;
	color: #E6E6E6;
	font-weight: bold;
	font-size: 5rem;
	align-items: center;
	justify-content: center;
	">
		<div style="
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		width: 80%;
		height: 80%;
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

<div style="
display: flex;
justify-content:center;
">
	<div style="
	background-color: #dddddd;
	max-width: 40ch;
	margin: 1rem;
	padding: 1rem;
	">
		Hello
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
</style>
