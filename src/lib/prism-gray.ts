import type {PrismTheme} from 'prism-react-renderer';

// Code highlighting without hue (DESIGN.md): weight and darkness only.
// Colors are CSS variables, so one theme follows light and dark mode.
const prismGray: PrismTheme = {
  plain: {
    color: 'var(--ink)',
    backgroundColor: 'var(--surface-2)',
  },
  styles: [
    {
      types: ['comment', 'prolog', 'doctype', 'cdata'],
      style: {color: 'var(--faint)', fontStyle: 'italic'},
    },
    {
      types: ['punctuation', 'operator'],
      style: {color: 'var(--muted)'},
    },
    {
      types: ['keyword', 'selector', 'important', 'atrule', 'builtin'],
      style: {fontWeight: '600'},
    },
    {
      types: ['string', 'char', 'attr-value', 'regex', 'url', 'inserted'],
      style: {color: 'var(--muted)'},
    },
    {
      types: ['number', 'boolean', 'constant', 'symbol'],
      style: {color: 'var(--muted)', fontWeight: '500'},
    },
    {
      types: ['function', 'class-name', 'tag'],
      style: {fontWeight: '500'},
    },
    {
      types: ['deleted'],
      style: {color: 'var(--faint)', textDecorationLine: 'line-through'},
    },
  ],
};

export default prismGray;
