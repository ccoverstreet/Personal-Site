<script>
	let abstractVisible = false;

	export let articleTitle = "";
	export let articleLink = ""
	export let journalName = "";
	export let abstract = "";
</script>

<div id="holder">
	<p><em><a href={articleLink}>{articleTitle}<a></em></p>
	<div id="contents">
		<p>{journalName}</p>
		<br>
		<button on:click={() => {abstractVisible = !abstractVisible}}>{#if abstractVisible}Abstract &gt{:else}Abstract &lt{/if} </button>
		<p id="abstract" hidden="{!abstractVisible}">{abstract}</p>
	</div>
</div>

<style>
	#holder {
		background-color: var(--clr-surface-1);
	}

	#abstract {
		padding: 1em;
		line-height: 2rem;
	}

	#contents {
		padding: 1em 1em 1em 1em;
	}

	button {
		background-color: #ffffff;
		padding: 0.5rem;
		border-radius: 0.5rem;
		margin-top: 0.25rem;
		margin-bottom: 0.25rem;
		background-color: var(--clr-secondary);
		color: var(--clr-font-light-high);
		border-width: 0;
	}

	button:hover {
		filter: brightness(70%);
	}
</style>

