import {InatagramEmbed} from 'react-social-media-embed';
const Instagramreels = () => {
  return (
    <div className="p-6 text-green-500">
      <h1 className="text-3xl font-bold">Instagram Reels</h1>
     <iframe
     width="400"
     height="600"
     src="https://api.instagram.com/oembed?url=https://www.instagram.com/reels/DZpMBymtMaz/"
     frameborder="0"
     scrolling="no"
     allowTransparency={true}
     >
     </iframe>
    </div>
  );
};

export default Instagramreels;