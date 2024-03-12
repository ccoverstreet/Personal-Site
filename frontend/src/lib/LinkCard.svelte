<script>
	export var title;
	export var subtitle;
	export var imageSrc;
	export var link;
</script>

<a href={link} style="text-decoration: none;">
	<div class="card">
		<div class="card-header">
			<h1>{title}</h1>
			<h2>{subtitle}</h2>
		</div>
		<img src={imageSrc} style="height: 24rem; width: 100%; object-fit: cover;"/>
	</div>
</a>

