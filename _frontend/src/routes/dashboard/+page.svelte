<script>
	import { goto } from '$app/navigation';
	import loginIcon from '$lib/icons/login.png';
	import auth from '$lib/services/auth';

	async function logout() {
		const client = await auth.createClient();

		await auth.logout(client);

		goto('/login?code=out');
	}
</script>

<div id="dashboard-container">
	<div id="logout">
		<button type="submit" on:click={logout}>
			<img id="logout-icon" src={loginIcon} alt="logout logo" />
		</button>
	</div>
	<div id="main-menu">
		<div id="profile" class="main-bubble">
			<div id="receipt-upload" />

			<div id="tracker" />

			<div id="coming-soon-1" />

			<div id="coming-soon-2" />

			<div id="coming-soon-3" />

			<div id="coming-soon-4" />

			<div id="coming-soon-5" />
		</div>
	</div>
</div>

<style lang="scss">
	#dashboard-container {
		position: relative;

		width: 100vw;
		height: 100vh;

		background-image: url('https://mergersandinquisitions.com/wp-content/uploads/2009/09/iStock-147286126.jpg');
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;

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
