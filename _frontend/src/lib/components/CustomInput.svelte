<script lang="ts">
	export let isNamed = false;
	export let type = 'text';
	export let placeholder = 'Name';
	export let value: string | File = 'Augusto Mota Pinheiro';
	export let processing = false;
	export let action: (e: Event) => void = () => {};

	const onFileSelected = (e: Event) => {
		if (type != 'file') {
			action(e);
			return;
		}

		processing = true;

		if (e.target == null) return;
		const htmlElement = e.target as HTMLInputElement;
		if (htmlElement.files == null) return;

		let image = htmlElement.files[0];
		value = image;
	};
</script>

<div id="input-container" {...$$props}>
	{#if isNamed}
		<p>{placeholder}</p>
	{/if}
	<input
		class={isNamed ? '' : 'alone'}
		{type}
		placeholder={isNamed ? '' : placeholder}
		value={type == 'file' ? '' : value}
		on:change={onFileSelected}
	/>
</div>

<style lang="scss">
	#input-container {
		width: 100%;

		display: grid;
		grid-template-columns: 30% 70%;
		gap: 2rem;

		margin-top: 0.75rem;

		font-family: 'Nanum Gothic', 'Gothic Medium';

		p {
			display: inline-block;

			justify-self: right;
		}

		input {
			display: inline-block;

			justify-self: left;

			width: 20rem;
			height: 2rem;

			padding: 0.5rem;

			border: 1px solid #000;
			border-radius: 5px;

			font-size: 1rem;
			font-weight: 700;
			color: #000;

			&:focus {
				outline: none;
			}

			&::placeholder {
				color: #8a8a8a;
			}

			&.alone {
				grid-column-start: 1;
				grid-column-end: 3;
				margin: 0 auto;
			}
		}
	}
</style>
