/* eslint-disable react/prop-types */
export function Description({avantages}) {
    return (
        <div>
            <h2>Description</h2>
            <p>React est une librairie javascript réée par facebook.</p>

            Avantages:
            <ul>
                {
                    avantages.map((avantage) => <li key={avantage.id}>{avantage.titre}</li>)
                }
            </ul>
        </div>
    );
}
