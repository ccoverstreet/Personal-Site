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
		border-radius: 0.5rem;
		padding: 0.5rem;
		margin: 0.5rem auto;
		display: block;
		width: min(120ch, calc(100% - 1em));
		background-color: var(--clr-surface-1);
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
