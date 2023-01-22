<script lang="ts">
	import CustomButton from '$lib/components/CustomButton.svelte';

	import loginIcon from '$lib/icons/login.png';

	import logo from '$lib/icons/logo.png';
	import auth from '$lib/services/auth';

	async function login() {
		let client = await auth.createClient();

		await auth.loginWithPopup(client);
	}
</script>

<div id="login-container">
	<div id="login-bg-filter">
		<div id="logo">
			<img src={logo} alt="logo" />
		</div>
		<div id="welcome">
			<div id="welcome-header" class="header">
				<h2>Welcome to WiseWallet</h2>
			</div>
			<div id="welcome-body">
				<p>
					WiseWallet helps you make the right purchasing decisions by delivering the internet's
					knowledge to the palm of your hand.
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
						<CustomButton class="c-control" value="Get Started" icon={loginIcon} action={login} />
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
		background-position: center;
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
				padding-right: 20%;

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
				box-shadow: $layout-shadow;

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
				}
			}
		}
	}
</style>
