<div>
	<h2>
		<slot name="title"></slot>
	</h2>
	<hr>
	<div>
		<slot name="content"></slot>
	</div>
</div>

<style>
	div {
		border-radius: 0.25rem;
		padding: 0.5em;
		display: inline-block;
		width: 100%;
	}

	div > div {
		margin: 0;
		padding: 1em;
	}

	h2 {
		padding-left: 1rem;
		font-size: 24px;
		font-weight: bold;
	}
</style>
