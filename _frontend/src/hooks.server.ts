import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async function ({ event, resolve }) {
	let token = event.url.searchParams.get('code');

	if (token == 'out') {
		event.cookies.delete('token');
		token = null;
	} else if (token == null) {
		token = event.cookies.get('token') ?? null;
	} else {
		event.cookies.set('token', token);
	}

	if (event.route.id != '/login' && token == null) {
		return Response.redirect(`${event.url.origin}/login`, 307);
	} else return await resolve(event);
};
