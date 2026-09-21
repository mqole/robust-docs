import React from 'react';
import Admonition from '@theme/Admonition';

export default function WipHeader(){
  return(
    <div>
      <Admonition type="info" title="Work in Progress">
        <p>This page is a work in progress. Information present here may be incomplete or outdated.</p>
      </Admonition>
    </div>
  );
};