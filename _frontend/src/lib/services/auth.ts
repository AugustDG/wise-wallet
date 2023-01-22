import { createAuth0Client, type Auth0Client } from '@auth0/auth0-spa-js';
import { user, isAuthenticated, popupOpen } from '../stores/auth';
import config from '../../auth.config';
import { setContext } from 'svelte';

async function createClient() {
	const auth0Client: Auth0Client = await createAuth0Client({
		domain: config.domain,
		clientId: config.clientId
	});

	return auth0Client;
}

async function loginWithPopup(client: Auth0Client) {
	popupOpen.set(true);

	try {
		await client.loginWithRedirect({
			authorizationParams: { prompt: 'login', redirect_uri: window.location.origin + '/dashboard' }
		});

		const fetchedUser = await client.getUser();

		user.set(fetchedUser);
		isAuthenticated.set(true);
	} catch (error) {
		console.error(error);
	} finally {
		popupOpen.set(false);
	}
}

function logout(client: Auth0Client) {
	return client.logout({ logoutParams: { returnTo: window.location.origin + '/login?code=out' } });
}

const auth = {
	createClient,
	loginWithPopup,
	logout
};

export default auth;
