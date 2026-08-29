import React from 'react';
import Layout from '@theme-original/Layout';
import type LayoutType from '@theme/Layout';
import type {WrapperProps} from '@docusaurus/types';
import Head from '@docusaurus/Head';

type Props = WrapperProps<typeof LayoutType>;

// Every app in this workspace shows just its own name in the browser tab, so
// arca does too - "arca", not "intro | arca".
//
// Docusaurus builds the tab title as `<page title> | <site title>`, and there
// is no config for dropping the page half. The override therefore has to be
// rendered *after* <Layout>, because react-helmet-async keeps the last <title>
// it is given, and the page's own metadata renders inside the layout.
export default function LayoutWrapper(props: Props): JSX.Element {
  return (
    <>
      <Layout {...props} />
      <Head>
        <title>arca</title>
      </Head>
    </>
  );
}
