import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: 'SS14 Development Docs',
  tagline: 'Unofficial documentation on developing stuff for that one space game.',
  favicon: 'img/favicon.ico',

  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  url: 'https://mqole.github.io',
  baseUrl: '/robust-docs/',
  organizationName: 'mqole',
  projectName: 'robust-docs',
  trailingSlash: false,

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  
  presets: [
    [
      'docusaurus-plugin-glossary/preset', // classic but with glossary support
      {
        docs: {
          routeBasePath: '/', // Serve the docs at the site's root
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/mqole/robust-docs/tree/main/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
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
        glossary: { // Glossary plugin
          glossaryPath: 'glossary/glossary.json',
          routePath: '/robust-docs/glossary',
        },
      }
    ],
  ],
  
  themeConfig: {
    image: 'img/logo.png',
    defaultMode: 'dark',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'SS14 Development Docs',
      logo: {
        alt: 'SS14 Development Docs logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'sidebar',
          position: 'left',
          label: 'Documents',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/mqole/robust-docs',
          label: 'GitHub',
          position: 'right',
        },
        { to: '/glossary', label: 'Glossary', position: 'left' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Documents',
              to: '/',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} mqole. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },

    // Mermaid:
    
    markdown: {
      mermaid: true,
    },
    
    themes: ['@docusaurus/theme-mermaid'],
    
    // KaTeX:
    
    stylesheets: [
      {
        href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css',
        type: 'text/css',
        integrity: 'sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLsoTkbqJghGIsx//Rlm+ZU03BU6SQNC66uf4l5+',
        crossorigin: 'anonymous',
      },
    ],
    
    scripts: [
      {
        src: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js",
        integrity: "sha384-7zkQWkzuo3B5mTepMUcHkMB5jZaolc2xDwL6VFqjFALcbeS9Ggm/Yr2r3Dy4lfFg",
        crossorigin: "anonymous",
        defer: true,
      },
      {
        src: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js",
        integrity: "sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTstBeZFe/+rCMvRwr4yROQP43s0Xk",
        crossorigin: "anonymous",
        defer: true,
      }
    ],

    plugins: [
      [require.resolve("docusaurus-lunr-search"), // lunr search. won't work in localenv.
        {enableHighlight: true}
      ]
    ],

  } satisfies Preset.ThemeConfig,
};

export default config;
