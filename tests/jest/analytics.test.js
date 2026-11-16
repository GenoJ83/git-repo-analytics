const { rankContributors, totalChurn } = require('../../js/analytics');

describe('Git Analytics', () => {
  it('ranks contributors by commit counts descending', () => {
    const commits = [{ author: 'Alice' }, { author: 'Bob' }, { author: 'Alice' }];
    const ranked = rankContributors(commits);
    expect(ranked[0][0]).toBe('Alice');
    expect(ranked[0][1]).toBe(2);
  });
  it('sums total code churn', () => {
    expect(totalChurn(50, 25)).toBe(75);
  });
});
