import { createFileRoute } from '@tanstack/react-router';
import { flavors, pageHead } from '@/lib/gelato';
import { FlavorCard } from '@/components/gelato/flavor-card';
export const Route = createFileRoute('/sabores')({ head:()=>pageHead('Nossos sabores','Explore os onze sabores artesanais da Gelato Vero, de morango e pistache às frutas tropicais.'), component: Sabores });
function Sabores() { return <div className="container catalog"><div className="page-heading"><div className="eyebrow">Uma colherada de felicidade</div><h1>Nossos sabores.</h1><p>Clássicos que acolhem, frutas que refrescam.<br />Encontre o sabor que combina com o seu momento.</p></div><div className="flavor-grid">{flavors.map(flavor=><FlavorCard key={flavor.name} flavor={flavor} />)}</div></div>; }
