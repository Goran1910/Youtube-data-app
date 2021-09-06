import { Playlist } from "./Playlist";

export interface Video{
    id: number,
    title: string,
    views: number,
    likes: number,
    dislikes: number,
    comments: number,
    publishedAt: Date,
    duration: number,
    thumbnailUrl: string,
    playlist: Playlist
    likesPercentage: number,
    likesAndDislikesPerView: number
}