import fs from 'node:fs/promises';
import path from 'node:path';
import type {LoadContext, Plugin} from '@docusaurus/types';

// Writes llms.txt (an index of every doc) and llms-full.txt (every doc's raw
// Markdown) to the build root. The Markdown is copied as written, so headings,
// code blocks and links stay the same. Runs on every `docusaurus build`.

type Doc = {
  title: string;
  description: string;
  permalink: string;
  source: string; // "@site/docs/..."
};

function stripFrontMatter(md: string): string {
  return md.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n+/, '');
}

export default function llmsTxtPlugin(context: LoadContext): Plugin {
  let docs: Doc[] = [];

  return {
    name: 'llms-txt',

    async allContentLoaded({allContent}) {
      const docsContent = allContent['docusaurus-plugin-content-docs']?.default as
        | {loadedVersions: {docs: Doc[]}[]}
        | undefined;
      docs = (docsContent?.loadedVersions[0]?.docs ?? [])
        // Numeric folder and file prefixes give the reading order.
        .slice()
        .sort((a, b) => a.source.localeCompare(b.source));
    },

    async postBuild({outDir}) {
      const {siteConfig} = context;
      const site = siteConfig.url.replace(/\/$/, '') + siteConfig.baseUrl.replace(/\/$/, '');
      const header = `# ${siteConfig.title}\n\n> ${siteConfig.tagline || 'Personal knowledge base'}\n`;

      const index = docs.map((d) => {
        const desc = d.description ? `: ${d.description}` : '';
        return `- [${d.title}](${site}${d.permalink})${desc}`;
      });

      const full: string[] = [];
      for (const d of docs) {
        const file = path.join(context.siteDir, d.source.replace(/^@site\//, ''));
        const body = stripFrontMatter(await fs.readFile(file, 'utf8')).trim();
        full.push(`<!-- source: ${site}${d.permalink} -->\n\n${body}\n`);
      }

      await fs.writeFile(
        path.join(outDir, 'llms.txt'),
        `${header}\n## Docs\n\n${index.join('\n')}\n`,
      );
      await fs.writeFile(path.join(outDir, 'llms-full.txt'), `${header}\n${full.join('\n---\n\n')}`);
    },
  };
}
