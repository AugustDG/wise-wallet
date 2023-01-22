<script>
	import accountIcon from '$lib/icons/account.png';
	import saveIcon from '$lib/icons/save.png';
	import savedIcon from '$lib/icons/saved.png';

	import { Modal, Content, Trigger } from 'sv-popup';
	import CustomInput from './CustomInput.svelte';
	import CustomButton from './CustomButton.svelte';
	import { fade } from 'svelte/transition';

	const fadeDuration = 200;

	let closed = false;
	let saving = false;

	function save() {
		saving = true;
		setTimeout(() => {
			saving = false;
		}, fadeDuration * 4);
	}
</script>

<Modal close={closed}>
	<Trigger>
		<div id="profile" class="main-bubble">
			<img src={accountIcon} alt="" />
		</div>
	</Trigger>
	<Content class="modal-container">
		<h2 class="c-control">Profile</h2>

		<CustomInput class="c-control" isNamed={true} placeholder="Name" />
		<CustomInput
			class="c-control"
			isNamed={true}
			placeholder="Address"
			value="1500, Atwater Ave, Montreal"
		/>
		<CustomInput class="c-control" isNamed={true} placeholder="Salary" value="90 000$" />

		<CustomButton class="c-control" value="Save" icon={saveIcon} action={save} />

		{#if saving}
			<div
				in:fade={{ duration: fadeDuration }}
				out:fade={{ duration: fadeDuration }}
				id="save-overlay"
			>
				<img src={savedIcon} alt="" />
			</div>
		{/if}
	</Content>
</Modal>

<style lang="scss" global>
	.modal-container {
		width: 45vw !important;
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

		#save-overlay {
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
		}
	}
</style>
