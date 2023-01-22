<script lang="ts">
	import { goto } from '$app/navigation';
	import loginIcon from '$lib/icons/login.png';
	import auth from '$lib/services/auth';
	import { isAuthenticated } from '$lib/stores/auth';
	import { page } from '$app/stores';
	import cookie from 'cookie';

	async function submit() {
		let client = await auth.createClient();

		await auth.loginWithPopup(client, {
			authorizationParams: { redirect_uri: 'http://localhost:5173' }
		});

		if ($isAuthenticated) {
			goto('/dashboard');
		}
	}
</script>

<div id="login-container">
	<div id="login-bg-filter">
		<div id="logo">
			<img
				src="https://marketplace.canva.com/EAE3ErRzI6g/1/0/1600w/canva-people-dollar-logo%2C-money-finances-logo-gdfxtb4mf80.jpg"
				alt="logo"
			/>
		</div>
		<div id="welcome">
			<div id="welcome-header" class="header">
				<h2>Welcome to Blended Finance</h2>
			</div>
			<div id="welcome-body">
				<p>
					Blended Finance helps you make the right purchasing decisions by delivering the internet's
					knowledge to your palm.
				</p>
			</div>
		</div>
		<div id="login-wrapper">
			<div id="login">
				<div id="login-header" class="header">
					<h1>Happy you're here :)</h1>
				</div>
				<div id="login-body">
					<div id="login-body-form">
						<button type="submit" on:click={submit}>
							<span>Get Started</span>
							<img id="login-icon" src={loginIcon} alt="login logo" /></button
						>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	#login-container {
		width: 100vw;
		height: 100vh;

		position: relative;

		background-image: url('https://www.thegef.org/sites/default/files/styles/banner_image/public/2021-11/topics_banner_blendedfinance.jpg?h=4e9a1ef8&itok=7cUg7zcQ');
		background-repeat: no-repeat;
		background-position: 50% 50%;
		background-size: cover;

		#logo {
			position: absolute;
			top: 4rem;
			left: 4rem;

			img {
				width: 5rem;
				height: 5rem;

				border-radius: 100%;
			}
		}

		#login-bg-filter {
			width: 100%;
			height: 100%;

			display: grid;
			grid-template-columns: 60% 40%;

			background: linear-gradient(
				90deg,
				rgba(0, 0, 0, 0.5) 0%,
				rgba(0, 0, 0, 0.5) 40%,
				rgba(0, 0, 0, 0) 100%
			);
		}

		#welcome {
			grid-column: 1;

			padding-left: 4rem;

			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: flex-start;

			#welcome-header {
				font-family: 'Unbounded', Georgia;

				h2 {
					font-size: 3rem;
					font-weight: 700;
					color: $white;
				}
			}

			#welcome-body {
				padding-right: 30%;

				font-family: 'Nanum Gothic', 'Gothic Medium';

				p {
					font-size: 1.5rem;
					font-weight: 700;
					color: $white;
				}
			}
		}

		#login-wrapper {
			grid-column: 2;

			display: flex;
			justify-content: center;
			align-items: center;

			#login {
				width: 20rem;
				margin-top: 2rem;
				padding: 5rem 3rem;

				border-radius: 7px;
				box-shadow: $layoutShadow;

				display: flex;
				justify-items: stretch;
				flex-direction: column;

				background-color: $white;

				#login-header {
					font-family: 'Unbounded', Georgia;

					h1 {
						text-align: center;

						font-size: 2rem;
						font-weight: 700;
						color: $black;
					}
				}

				#login-body {
					margin: 0;

					#login-body-form {
						button {
							font-family: 'Nanum Gothic', 'Gothic Medium';
							font-weight: 700;

							width: 100%;
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
								box-shadow: $buttonShadow;
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
					}
				}
			}
		}
	}
</style>
