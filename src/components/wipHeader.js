import React from 'react';
import Admonition from '@theme/Admonition';

export default function WipHeader({text}){
  return(
    <div>
      <Admonition type="info" title="Work in Progress">
        <p>This page is a work in progress. Information present here may be incomplete or outdated.</p>
        <p>{text}</p>
      </Admonition>
    </div>
  );
};