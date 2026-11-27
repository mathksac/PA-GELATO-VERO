import morango from '@/assets/morango.jpg';
import creme from '@/assets/creme.jpg';
import chocolate from '@/assets/chocolate.jpg';
import pistache from '@/assets/pistache.jpg';
import maracuja from '@/assets/maracuja.jpg';
import limao from '@/assets/limao.jpg';
import manga from '@/assets/manga.jpg';
import coco from '@/assets/coco.jpg';
import uva from '@/assets/uva.jpg';
import abacaxi from '@/assets/abacaxi.jpg';
import frutas from '@/assets/frutas-vermelhas.jpg';
export const flavors = [
 { name: 'Morango', image: morango, description: 'O sabor marcante dos morangos naturais, em uma textura irresistivelmente cremosa.', best: true },
 { name: 'Creme', image: creme, description: 'Um clássico suave e delicado. A simplicidade que conquista a cada colherada.', best: true },
 { name: 'Chocolate', image: chocolate, description: 'Intenso, cremoso e cheio de sabor. Um encontro especial com o chocolate.', best: true },
 { name: 'Pistache', image: pistache, description: 'Delicado e especial, com o sabor característico do verdadeiro pistache.', best: true },
 { name: 'Maracujá', image: maracuja, description: 'O equilíbrio entre o doce e o azedinho da fruta.' , best: false },
 { name: 'Limão', image: limao, description: 'Leve e refrescante, com um toque cítrico natural.', best: false },
 { name: 'Manga', image: manga, description: 'O sabor tropical e a doçura natural da manga.', best: false },
 { name: 'Coco', image: coco, description: 'Suave e cremoso, com todo o sabor do coco.', best: false },
 { name: 'Uva', image: uva, description: 'A intensidade da fruta em uma colherada cheia de frescor.', best: false },
 { name: 'Abacaxi', image: abacaxi, description: 'Tropical e refrescante, com a acidez delicada do abacaxi.', best: false },
 { name: 'Frutas vermelhas', image: frutas, description: 'Uma combinação de frutas com sabor delicado e marcante.', best: false },
];
export function pageHead(title: string, description: string) {
 return { meta: [{ title: `${title} | Gelato Vero` }, { name: 'description', content: description }, { property: 'og:title', content: `${title} | Gelato Vero` }, { property: 'og:description', content: description }, { property: 'og:type', content: 'website' }, { name: 'twitter:card', content: 'summary_large_image' }] };
}
