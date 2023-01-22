<script>
	import graphIcon from '$lib/icons/graph.png';
	import saveIcon from '$lib/icons/save.png';
	import loadingIcon from '$lib/icons/loading_static.png';

	import { Modal, Content, Trigger } from 'sv-popup';
	import CustomInput from './CustomInput.svelte';
	import CustomButton from './CustomButton.svelte';
	import { fade } from 'svelte/transition';

	const fadeDuration = 200;

	let closed = false;
	let loading = false;

	function loadData() {
		loading = true;
		setTimeout(() => {
			loading = false;
		}, fadeDuration * 8);
	}
</script>

<Modal close={closed}>
	<Trigger>
		<div id="tracker" class="second-bubble b-2">
			<img src={graphIcon} alt="" />
		</div>
	</Trigger>
	<Content class="modal-container">
		<h2 class="c-control">Tracker</h2>

		<CustomButton class="c-control" value="Load" icon={saveIcon} action={loadData} />

		{#if loading}
			<div
				in:fade={{ duration: fadeDuration }}
				out:fade={{ duration: fadeDuration }}
				id="loading-overlay"
			>
				<img src={loadingIcon} alt="" />
			</div>
		{/if}
	</Content>
</Modal>

<style lang="scss" global>
	.modal-container {
		width: 75vw !important;
		height: 75vh;
		padding: 20px 20px 2.5rem 20px;

		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;

		font-family: 'Nanum Gothic', 'Gothic Medium';

		border-radius: $layout-border-radius;
		box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);

		background-color: #fff;

		.c-control {
			z-index: -2;
		}

		h2 {
			font-family: 'Unbounded', Georgia;
		}

		#loading-overlay {
			z-index: -1;

			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;

			display: flex;
			justify-content: center;
			align-items: center;

			overflow: hidden;

			border-radius: $layout-border-radius;

			background-color: $white;

			& > img {
				animation: rotate 3s linear infinite;
			}
		}

		@keyframes rotate {
			0% {
				transform: rotate(0deg);
			}
			100% {
				transform: rotate(360deg);
			}
		}
	}
</style>
