<script>
	export var imageName;
	export var description;
</script>

<div style="margin: 0.25rem; padding: 0.25rem; background-color: #ffffff; box-shadow: 0.25rem 0.25rem 1rem black;">
	<img src={imageName} style="width: 100%; min-width: 15rem;height: auto; max-width: 20rem; object-fit: cover;"/>
	<p style="text-align: center; color: #222222">{description}</p>
</div>


<style>
	img {
		width: 100%;
	}
</style>
