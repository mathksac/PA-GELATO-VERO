import type { flavors } from '@/lib/gelato';
export function FlavorCard({ flavor }: { flavor: (typeof flavors)[number] }) {
 return <article className="flavor-card"><div className="flavor-photo"><img src={flavor.image} alt={`Sorvete artesanal de ${flavor.name.toLowerCase()}`} loading="lazy" />{flavor.best && <span className="best-label">Mais vendidos</span>}</div><div className="flavor-content"><h3>{flavor.name}</h3><p>{flavor.description}</p></div></article>;
}
