<script lang="ts">
	import graphIcon from '$lib/icons/graph.png';
	import syncIcon from '$lib/icons/sync.png';
	import loadingIcon from '$lib/icons/loading_static.png';

	import { Modal, Content, Trigger } from 'sv-popup';
	import CustomInput from './CustomInput.svelte';
	import CustomButton from './CustomButton.svelte';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';

	const fadeDuration = 200;

	let closed = false;
	let loading = false;
	let searchQuery = '';

	let rawItems: {
		id: number;
		fruit: string;
		curPrice: number;
		bestPrice: number;
		bestPriceUrl: string;
	}[] = [];

	$: items = rawItems;

	onMount(async () => {
		await loadData();
	});

	function search(e: Event) {
		searchQuery = (e.target as HTMLInputElement).value;
		loading = true;
		items = rawItems.filter((item) =>
			item.fruit.toLocaleLowerCase().includes(searchQuery.toLocaleLowerCase())
		);
		loading = false;
	}

	async function loadData() {
		const body = JSON.stringify([
			{
				fruit: 'apple',
				curPrice: 2.99,
				bestPrice: 1.99,
				bestPriceUrl: ''
			},
			{
				fruit: 'banana',
				curPrice: 2.99,
				bestPrice: 1.99,
				bestPriceUrl: ''
			},
			{
				fruit: 'orange',
				curPrice: 2.99,
				bestPrice: 1.99,
				bestPriceUrl: ''
			},
			{
				fruit: 'kiwi',
				curPrice: 2.99,
				bestPrice: 1.99,
				bestPriceUrl: ''
			}
		]);

		await fetch('http://localhost:8080/item/checkPrices', {
			method: 'POST',
			body: body,
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then((data) => {
				rawItems = data;
			})
			.catch((err) => {
				console.log(err);
			});
	}

	async function refresh() {
		loading = true;
		await loadData();
		loading = false;
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

		<CustomInput class="c-control" placeholder="Search" action={search} bind:value={searchQuery} />

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

		<CustomButton class="c-control" value="Refresh" icon={syncIcon} action={refresh} />

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
		padding: 20px 2rem 2.5rem 2rem;

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

		h2,
		.item {
			font-family: 'Unbounded', Georgia;
		}

		#items {
			width: 70%;
			margin: 1rem auto 0 auto;

			hr {
				width: 70%;
				margin: auto;
			}

			.item {
				display: grid;
				grid-template-columns: 40% 30% 30%;
				gap: 1rem;

				text-transform: capitalize;
				text-align: left;

				.your-price,
				.best-price {
					text-align: right;
				}

				.best-price a {
					color: $primary;
					text-decoration: none;

					&:hover {
						cursor: pointer;
						filter: brightness(1.2);
						text-decoration: underline;
					}

					&:active {
						#login-icon {
							filter: brightness(0.8);
						}
					}
				}
			}
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
