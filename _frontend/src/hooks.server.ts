import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async function ({ event, resolve }) {
	let token = event.url.searchParams.get('code');

	if (token == null || token == '') token = event.cookies.get('token') ?? null;
	else event.cookies.set('token', token);

	if (token == null && event.route.id !== '/login') {
		return Response.redirect(`${event.url.origin}/login`, 307);
	}

	return await resolve(event);
};
