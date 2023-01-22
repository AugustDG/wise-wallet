<script>
	export let action = () => {};
	export let icon = '';
	export let value = 'Click me!';
	export let customContent = false;
</script>

<div id="input-container" class={$$props.class}>
	<button type="submit" on:click={action}>
		{#if customContent}
			<slot />
		{:else}
			<span>{value}</span>
		{/if}
		<img id="login-icon" src={icon} alt="icon" /></button
	>
</div>

<style lang="scss">
	button {
		font-weight: 700;

		width: 100%;
		min-width: 6.5rem;
		margin-top: 2rem;
		margin-left: auto;
		margin-right: auto;
		padding: 0.5rem 0.6rem;

		display: flex;
		justify-content: center;
		align-content: center;
		align-items: center;
		gap: 0.5rem;

		border-style: solid;
		border-width: 2px;
		border-radius: 3px;
		border-color: $black;

		text-transform: uppercase;

		background-color: $black;
		color: $white;

		&:hover {
			cursor: pointer;
			filter: brightness(1.2);
			box-shadow: $button-shadow;
		}

		&:active {
			#login-icon {
				filter: brightness(0.8);
			}
		}

		#login-icon {
			aspect-ratio: 1;
			height: 1.5rem;
		}
	}
</style>
