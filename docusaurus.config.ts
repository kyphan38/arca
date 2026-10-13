import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import prismGray from './src/lib/prism-gray';

const config: Config = {
  title: 'arca',
  favicon: 'img/favicon.svg',

  url: 'https://kyphan38.github.io',
  baseUrl: '/',

  organizationName: 'arca',
  projectName: 'arca',
  deploymentBranch: 'gh-pages',

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
    [
      require.resolve("@cmfcmf/docusaurus-search-local"),
      {
        indexDocs: true,
        indexBlog: true,
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
    navbar: {
      title: 'arca',
      logo: {
        alt: 'arca',
        src: 'img/branding/arca-icon.svg',
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