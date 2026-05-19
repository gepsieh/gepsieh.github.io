// Cloudflare Worker: GitHub OAuth Token Exchange Proxy
// Deploy to long-moon-1aef.314308943.workers.dev
//
// Required secrets (set via `wrangler secret put` or Cloudflare Dashboard):
//   GITHUB_CLIENT_ID     - GitHub OAuth App client ID
//   GITHUB_CLIENT_SECRET - GitHub OAuth App client secret
//
// Expected flow:
//   1. User clicks "Login" on admin page
//   2. Redirected to GitHub OAuth (redirect_uri = this worker /callback)
//   3. GitHub redirects back here with ?code=xxx&state=xxx
//   4. Worker exchanges code for token (server-side, secret never exposed)
//   5. Worker redirects to admin page with token in URL hash

const ADMIN_URL = 'https://gepsieh.github.io/admin/';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // OAuth callback endpoint
    if (url.pathname === '/callback') {
      const code = url.searchParams.get('code');
      const state = url.searchParams.get('state');

      if (!code) {
        return new Response('Missing authorization code', { status: 400 });
      }

      try {
        const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          body: JSON.stringify({
            client_id: env.GITHUB_CLIENT_ID,
            client_secret: env.GITHUB_CLIENT_SECRET,
            code: code,
          }),
        });

        const data = await tokenResponse.json();

        if (data.error) {
          return new Response('OAuth Error: ' + (data.error_description || data.error), { status: 400 });
        }

        if (!data.access_token) {
          return new Response('No access token received from GitHub', { status: 500 });
        }

        // Redirect back to admin page with token in URL hash
        const redirectUrl = ADMIN_URL + '#access_token=' + encodeURIComponent(data.access_token)
          + (state ? '&state=' + encodeURIComponent(state) : '');

        return Response.redirect(redirectUrl, 302);
      } catch (err) {
        return new Response('Token exchange failed: ' + err.message, { status: 500 });
      }
    }

    // Health check
    if (url.pathname === '/health') {
      return new Response('ok');
    }

    return new Response('Not Found', { status: 404 });
  },
};
