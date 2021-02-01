class NewsAgent:
    def search_by_title(self, title) :
        """ Returns a dictionary of news articles

            For example:

            return [
                {
                    title: "Lockdown: Level 4 extended by two weeks",
                    desc: "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                    link: "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                },
                {
                    title: "Zinara toll fees to move with exchange rate",
                    desc: "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                    link: "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                },
            ]
        
        """
        return [
                    {
                        'title': "Lockdown: Level 4 extended by two weeks",
                        'desc': "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                        'link': "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                    },
                    {
                        'title': "Zinara toll fees to move with exchange rate",
                        'desc': "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                        'link': "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                    },
                ]

    def search_by_category(self, cat) :
        """ Returns a dictionary of news articles

            For example:

            return [
                {
                    title: "Lockdown: Level 4 extended by two weeks",
                    desc: "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                    link: "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                },
                {
                    title: "Zinara toll fees to move with exchange rate",
                    desc: "Herald Reporters The national lockdown will continue at level four for a further two weeks to February 15 to consolidate ... ",
                    link: "https://www.herald.co.zw/zinara-toll-fees-to-move-with-exchange-rate/"
                },
            ]
        
        """
        raise NotImplementedError



