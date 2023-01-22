import adapter from '@sveltejs/adapter-node';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: preprocess({
		typescript: {
			tsconfigFile: './tsconfig.json'
		},
		scss: {
			prependData: '@use "sass:math" as math; @import "src/styles/_main.scss";'
		}
	}),

	kit: {
		adapter: adapter(),
	}
};

export default config;
