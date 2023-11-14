import React from 'react';

const TokenInfo = ({ tokenData }) => {
  return (
    <div className="token-info-container">
      {tokenData.map((token, index) => (
        <div key={index} className="token-card">
          <h3>{`Token ${index + 1}: ${token.Token}`}</h3>
          <div className="info-row">
            <strong>Dependency Parsing:</strong> {`Dependency: ${token.DependencyParsing.Dependency}, Head Token: ${token.DependencyParsing.HeadText}`}
          </div>
          <div className="info-row"><strong>Is Numeric:</strong> {`${token.IsNumeric}`}</div>
          <div className="info-row"><strong>Is Punctuation:</strong> {`${token.IsPunctuation}`}</div>
          <div className="info-row"><strong>Is Space:</strong> {`${token.IsSpace}`}</div>
          <div className="info-row"><strong>Is Stop Word:</strong> {`${token.IsStopWord}`}</div>
          <div className="info-row"><strong>Lemma:</strong> {`${token.Lemma}`}</div>
          <div className="info-row">
            <strong>NER:</strong> {`Entity Type: ${token.NER.EntityType}, IOB Code: ${token.NER.IOBCode}`}
          </div>
          <div className="info-row"><strong>Position in Sentence:</strong> {`${token.PositionInSentence}`}</div>
          <div className="info-row"><strong>Sentence Index:</strong> {`${token.SentenceIndex}`}</div>
          <div className="info-row"><strong>Similarity to 'Processing':</strong> {`${token.SimilarityToProcessing}`}</div>
          <div className="info-row"><strong>Word Shape:</strong> {`${token.WordShape}`}</div>
        </div>
      ))}
    </div>
  );
};

export default TokenInfo;
