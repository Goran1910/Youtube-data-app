import { Channel } from "./Channel";

export interface Playlist{
    title: string,
    id: string,
    thumbnailUrl: string,
    channel: Channel,
    totalViews: number,
    totalLikes: number,
    totalDislikes: number,
    totalComments: number,
    likesPercentage: number,
    likesAndDislikesPerView: number
}