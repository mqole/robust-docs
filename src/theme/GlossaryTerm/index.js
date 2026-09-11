import React from 'react';
import GlossaryTerm from '@theme-original/GlossaryTerm';
import styles from '../../css/styles.module.css';

export default function GlossaryTermWrapper(props) {
  return (
    <>
      <glossaryStyle className={styles.glossaryStyle}><GlossaryTerm {...props} /></glossaryStyle>
    </>
  );
}
