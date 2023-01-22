<script lang="ts">
	import logo from '$lib/icons/logo.png';
	import loginIcon from '$lib/icons/login.png';
	import graphIcon from '$lib/icons/graph.png';
	import workIcon from '$lib/icons/work.png';

	import { goto } from '$app/navigation';
	import auth from '$lib/services/auth';
	import UserModal from '$lib/components/UserModal.svelte';
	import ReceiptModal from '$lib/components/ReceiptModal.svelte';
	import StatsModal from '$lib/components/StatsModal.svelte';

	async function logout() {
		const client = await auth.createClient();

		await auth.logout(client);

		goto('/login?code=out');
	}
</script>

<div id="dashboard-container">
	<div id="logo">
		<img src={logo} alt="logo" />
	</div>
	<div id="main-menu">
		<div id="bubbles-wrapper">
			<UserModal />

			<ReceiptModal />

			<StatsModal />

			<div id="coming-soon" class="second-bubble b-3">
				<img src={workIcon} alt="" />
			</div>

			<div id="coming-soon" class="second-bubble b-4">
				<img src={workIcon} alt="" />
			</div>

			<div id="coming-soon" class="second-bubble b-5">
				<img src={workIcon} alt="" />
			</div>
		</div>
	</div>
	<div id="logout">
		<button type="submit" on:click={logout}>
			<img id="logout-icon" src={loginIcon} alt="logout logo" />
		</button>
	</div>
</div>

<style lang="scss" global>
	#dashboard-container {
		position: relative;

		width: 100vw;
		height: 100vh;

		background-image: url('https://mergersandinquisitions.com/wp-content/uploads/2009/09/iStock-147286126.jpg');
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;

		#logo {
			position: absolute;
			top: 6vh;
			left: 4vw;

			img {
				width: 5rem;
				height: 5rem;
			}
		}

		#main-menu {
			width: 100%;
			height: 100%;

			background-color: rgba(0, 0, 0, 0.5);

			#bubbles-wrapper {
				width: inherit;
				height: inherit;

				position: relative;

				.main-bubble > img,
				.second-bubble > img {
					aspect-ratio: 1;
					width: 100%;
				}

				#receipt-upload > img {
					width: 75%;
				}

				#tracker > img {
					width: 70%;
				}

				#coming-soon {
					filter: brightness(0.8);
					& > img {
						width: 70%;
					}

					&:hover {
						cursor: not-allowed;
					}
				}

				.main-bubble,
				.second-bubble {
					display: flex;
					justify-content: center;
					align-items: center;

					font-size: 3rem;
					font-weight: 700;

					color: $primary;
					background-color: $white;

					box-shadow: $layout-shadow;

					&:hover {
						cursor: pointer;
						filter: brightness(1.2);
					}

					&:active {
						filter: brightness(0.8);
					}
				}

				.main-bubble {
					$bubble-size: 190px;

					aspect-ratio: 1;
					width: $bubble-size;
					border-radius: 50%;

					position: absolute;
					top: calc(50vh - $bubble-size / 2);
					left: calc(50vw - $bubble-size / 2);
				}

				.second-bubble {
					$bubble-size: 160px;

					aspect-ratio: 1;
					width: $bubble-size;
					border-radius: 50%;

					position: absolute;
					top: calc(50vh - $bubble-size / 2);
					left: calc(50vw - $bubble-size / 2);
				}

				@for $i from 1 through 5 {
					$angle: 72deg * $i - 18deg;
					$distance: 225px;

					$initial-x-position: math.cos($angle) * $distance;
					$initial-y-position: math.sin($angle) * $distance;

					@keyframes floating-#{$i} {
						0% {
							transform: translate($initial-x-position, $initial-y-position);
						}
						25% {
							transform: translate(
								$initial-x-position - math.cos($angle) * 10px,
								$initial-y-position + math.sin($angle) * 10px
							);
						}
						50% {
							transform: translate(
								$initial-x-position + math.cos($angle) * 10px,
								$initial-y-position - math.sin($angle) * 10px
							);
						}
						75% {
							transform: translate($initial-x-position, $initial-y-position);
						}
					}

					.second-bubble.b-#{$i} {
						$delay: 0.1s;

						transform: rotate($angle) translate($distance) rotate(-$angle);
						animation-name: floating-#{$i};
						animation-timing-function: linear;
						animation-duration: 12s;
						animation-fill-mode: forwards;
						animation-iteration-count: infinite;
						animation-delay: $delay;
					}
				}
			}
		}

		#logout {
			position: absolute;
			top: 6vh;
			right: 4vw;

			button {
				padding: 1rem;

				border-style: none;
				border-radius: 50%;

				box-shadow: $layout-shadow;

				background-color: $white;

				&:hover {
					cursor: pointer;
					filter: brightness(1.2);
				}

				&:active {
					#logout-icon {
						filter: brightness(0.8);
					}
				}
			}
		}
	}
</style>
