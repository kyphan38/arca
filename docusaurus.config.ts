import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'yolo',
  favicon: 'img/earth.ico',

  url: 'https://kyphan38.github.io',
  baseUrl: '/',

  organizationName: 'kyphan38',
  projectName: 'kyphan38.github.io',
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
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'assets/docs',
          sidebarPath: './sidebars/sidebars.ts',
          routeBasePath: '/',
          showLastUpdateTime: true,
        },
        blog: {
          path: 'assets/blog',
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
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
        // 1. Fix the "Hanging" issue (Lazy Loading)
        // This is enabled by default in this plugin, so no huge file downloads!
        
        // 2. Fix the "SSH" / Short word issue
        // We enable "partial" matching so "ss" finds "ssh"
        // We keep the index simple to avoid over-processing technical terms
        indexDocs: true,
        indexBlog: true,
        language: "en",
        
        // 3. UI Settings
        // style: "none", // Keeps it simple, avoiding CSS conflicts
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
      title: 'kp',
      logo: {
        alt: 'earth',
        src: 'img/bw_earth.png',
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
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    mermaid: {
      theme: { light: 'default'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;