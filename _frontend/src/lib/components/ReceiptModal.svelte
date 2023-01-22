<script lang="ts">
	import receiptIcon from '$lib/icons/receipt.png';
	import saveIcon from '$lib/icons/save.png';
	import savedIcon from '$lib/icons/saved.png';

	import { Modal, Content, Trigger } from 'sv-popup';
	import CustomInput from './CustomInput.svelte';
	import CustomButton from './CustomButton.svelte';
	import { fade } from 'svelte/transition';

	const fadeDuration = 200;

	let currentDateString = new Date().toDateString();
	let closed = false;
	let uploading = false;
	let analysis = false;
	let file: File | ArrayBuffer | null = null;
	$: hasFileError = false;
	let items = [
		{
			fruit: 'apple',
			curPrice: 2.99,
			bestPrice: 1.99,
			bestPriceUrl:
				'https://www.metro.ca/en/online-grocery/aisles/fruits-vegetables/fruits/apples-pears/mcintoshapple/p/4152'
		},
		{
			fruit: 'banana',
			curPrice: 2.99,
			bestPrice: 3.99,
			bestPriceUrl:
				'https://www.metro.ca/en/online-grocery/aisles/fruits-vegetables/fruits/bananas-plantains/banana/p/4011'
		},
		{
			fruit: 'orange',
			curPrice: 5.99,
			bestPrice: 4.99,
			bestPriceUrl:
				'https://www.metro.ca/en/online-grocery/aisles/fruits-vegetables/fruits/citrus-fruits/navel-oranges/p/033383119427'
		}
	];

	function done() {
		analysis = false;
	}

	function upload() {
		if (file == null) {
			hasFileError = true;
			console.log(hasFileError);
			return;
		}

		hasFileError = false;

		uploading = true;
		setTimeout(() => {
			uploading = false;
			analysis = true;
		}, fadeDuration * 8);

		file = null;
	}
</script>

<Modal close={closed}>
	<Trigger>
		<div id="receipt-upload" class="second-bubble b-1">
			<img src={receiptIcon} alt="" />
		</div>
	</Trigger>
	<Content class="modal-container">
		<h2 class="c-control">Upload Receipt</h2>

		{#if analysis}
			<div id="items">
				<div class="item">
					<p class="item-name">Item</p>
					<p class="your-price">Your Price</p>
					<p class="best-price">Best Price</p>
				</div>
				{#each items as it}
					<div class="item">
						<p class="item-name">{it.fruit}</p>
						<p class="your-price">{it.curPrice}$</p>
						<p class="best-price">
							<a target="_blank" href={it.bestPriceUrl}>{it.bestPrice}$</a>
						</p>
					</div>
				{/each}
			</div>

			<CustomButton class="c-control" value="Done" icon={saveIcon} action={done} />
		{:else}
			<CustomInput
				type="file"
				class="c-control"
				isNamed={false}
				placeholder="Receipt"
				bind:value={file}
			/>

			{#if hasFileError}
				<p class="error">Please upload a receipt</p>
			{/if}

			<CustomInput class="c-control" isNamed={true} placeholder="Date" value={currentDateString} />

			<CustomButton class="c-control" value="Upload" icon={saveIcon} action={upload} />
		{/if}

		{#if uploading}
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

		.error {
			margin-top: 0.2rem;
			margin-bottom: 0.1rem;
			color: $error;
			font-size: 0.8rem;
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
