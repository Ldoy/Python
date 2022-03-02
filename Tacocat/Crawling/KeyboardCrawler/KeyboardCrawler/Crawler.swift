//
//  Crawler.swift
//  KeyboardCrawler
//
//  Created by Do Yi Lee on 2022/02/28.
//

import Foundation
import SwiftSoup

enum CrawerError: Error {
    case addressInvalid
}

enum URLAdderess {
    case KarrotMarketKeyBoard
    
    var urlTex: String {
        switch self {
        case .KarrotMarketKeyBoard:
            return "https://www.daangn.com/search/기계식키보드"
        }
    }
}

class Crawler<Address> {
    let urlAddress: Address
    private (set)var result: [String] = []
    
    init(url: Address) {
        self.urlAddress = url
    }
}

extension Crawler where Address == URLAdderess {
    private func generateURL() throws -> URL {
        guard let urlAddress = self.urlAddress as? URLAdderess,
              let encodedURL = urlAddress.urlTex .addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed),
              let url = URL(string: encodedURL) else {
            print("url오류")
            throw CrawerError.addressInvalid
        }
        return url
    }
    
    private func generateDocument() -> Document? {
        do {
            let url = try generateURL()
            let html = try String(contentsOf: url, encoding: .utf8)
            let document: Document = try SwiftSoup.parse(html)
            print(html)
            return document
        } catch(let error) {
            print(error.localizedDescription)
            
            return nil
        }
    }
    
    func bringInformation() -> [String] {
        let emptyArray: [String] = []
        guard let document = generateDocument() else {
            return emptyArray
        }
        
        do {
            let headerTitle = try document.title()
            print(headerTitle)
            let objectTitle = try document.select(".article-title-content")
            for title in objectTitle {
                print(try title.text())
            }
            return [try objectTitle.text()]

        } catch {
            print(error)
            return emptyArray
        }
    }
}
