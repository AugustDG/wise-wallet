import { createAuth0Client, type PopupLoginOptions, type Auth0Client } from '@auth0/auth0-spa-js';
import { user, isAuthenticated, popupOpen } from '../stores/auth';
import config from '../../auth.config';

async function createClient() {
	const auth0Client: Auth0Client = await createAuth0Client({
		domain: config.domain,
		clientId: config.clientId
	});

	return auth0Client;
}

async function loginWithPopup(client: Auth0Client, options: PopupLoginOptions) {
	popupOpen.set(true);

	try {
		await client.loginWithPopup(options);

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
	return client.logout();
}

const auth = {
	createClient,
	loginWithPopup,
	logout
};

export default auth;
