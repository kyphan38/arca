import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import prismGray from './src/lib/prism-gray';
import llmsTxtPlugin from './src/plugins/llms-txt';

const config: Config = {
  title: 'arca',
  tagline: 'Personal knowledge base - notes on foundations, technologies and tools',
  favicon: 'img/favicon.svg',

  url: 'https://arca.kyphan38.com',
  baseUrl: '/',

  organizationName: 'arca',
  projectName: 'arca',
  deploymentBranch: 'gh-pages',

  future: {
    // Docusaurus Faster: Rspack bundler, SWC loader and minifiers, Lightning CSS.
    faster: {
      swcJsLoader: true,
      swcJsMinimizer: true,
      // @swc/html native binding fails on Cloudflare Pages (ERR_SWC_NATIVE_CACHE:
      // the build home is writable by another user). Use the JS HTML minifier.
      swcHtmlMinimizer: false,
      lightningCssMinimizer: true,
      mdxCrossCompilerCache: true,
      rspackBundler: true,
      rspackPersistentCache: true,
      ssgWorkerThreads: true,
      gitEagerVcs: true,
    },
    v4: {
      removeLegacyPostBuildHeadAttribute: true,
      useCssCascadeLayers: false,
    },
  },

  trailingSlash: false,
  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  headTags: [
    {
      tagName: 'meta',
      attributes: {
        name: 'robots',
        content: 'noindex, nofollow',
      },
    },
    // Browser bar follows the page background (DESIGN.md).
    {
      tagName: 'meta',
      attributes: {name: 'theme-color', content: '#fafafa', media: '(prefers-color-scheme: light)'},
    },
    {
      tagName: 'meta',
      attributes: {name: 'theme-color', content: '#111111', media: '(prefers-color-scheme: dark)'},
    },
    // Home screen icon and name for the PWA (iOS reads apple-touch-icon, not the manifest).
    {tagName: 'link', attributes: {rel: 'manifest', href: '/manifest.webmanifest'}},
    {tagName: 'link', attributes: {rel: 'apple-touch-icon', href: '/icons/apple-touch-icon.png'}},
    {tagName: 'meta', attributes: {name: 'apple-mobile-web-app-title', content: 'arca'}},
    {tagName: 'meta', attributes: {name: 'mobile-web-app-capable', content: 'yes'}},
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          sidebarPath: './sidebars/sidebars.ts',
          routeBasePath: '/',
          showLastUpdateTime: true,
        },
        blog: false,
        sitemap: {
          lastmod: 'date',
          changefreq: null,
          priority: null,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: [
    '@docusaurus/theme-mermaid',
  ],

  plugins: [
    llmsTxtPlugin,
    [
      '@docusaurus/plugin-client-redirects',
      {
        // Old links keep working after a page or folder is renamed.
        redirects: [
          {from: '/guides/vim', to: '/tools/vim'},
          {from: '/technologies/linux/ssh/main', to: '/technologies/linux/ssh'},
        ],
      },
    ],
    [
      require.resolve("@cmfcmf/docusaurus-search-local"),
      {
        indexDocs: true,
        indexBlog: false,
        indexPages: false,
        language: "en",
      },
    ],
  ],

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themeConfig: {
    // og:image and twitter:image for every page.
    image: 'img/social-card.png',
    metadata: [{name: 'twitter:card', content: 'summary_large_image'}],
    navbar: {
      title: 'arca',
      logo: {
        alt: 'arca logo',
        src: 'img/branding/arca-icon.svg',
        width: 32,
        height: 32,
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'docs',
        },
      ],
    },
    prism: {
      theme: prismGray,
      darkTheme: prismGray,
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'dark'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;