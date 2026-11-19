import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import prismGray from './src/lib/prism-gray';
import llmsTxtPlugin from './src/plugins/llms-txt';

const config: Config = {
  title: 'arca',
  tagline: 'Personal knowledge base - notes on foundations, technologies and guides',
  favicon: 'img/favicon.svg',

  url: 'https://kyphan38.github.io',
  baseUrl: '/',

  organizationName: 'arca',
  projectName: 'arca',
  deploymentBranch: 'gh-pages',

  future: {
    // Docusaurus Faster: Rspack bundler, SWC loader and minifiers, Lightning CSS.
    faster: true,
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