import { isAuthenticated } from './lib/stores/auth';
import { get } from 'svelte/store';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async function ({ event, resolve }) {
	console.log('handle', event);

	if (!get(isAuthenticated) && event.route.id !== '/login') {
		return Response.redirect(`${event.url.origin}/login`, 307);
	}

	return await resolve(event);
};
